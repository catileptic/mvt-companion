import json
from datetime import datetime
from pathlib import Path

from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import ScanResult, OSes
from .models import ANDROID, IOS, UNKNOWN, WARNING, CLEAN


def index(request):
    scan_result_dir_list = ScanResult.objects.order_by("-date_added")

    context = {"scan_result_dir_list": scan_result_dir_list}

    return render(request, "analyzer/upload.html", context)


def load_scan_results(request):
    p = Path("./mvt_output")

    if not p.exists():
        p.mkdir()

    scan_result_dir_list = [x for x in p.iterdir() if x.is_dir()]

    # TODO - the backup name must be unique
    if scan_result_dir_list:
        for scan_result_dir in scan_result_dir_list:
            scan_result_name = scan_result_dir.parts[-1]

            # get MVT version
            with open(scan_result_dir / "info.json", "r") as f:
                data = json.loads(f.read())
                mvt_version = data["mvt_version"]

            with open(scan_result_dir / "command.log", "r") as f:
                lines = f.readlines()
                # get operating system
                if ANDROID in lines[0]:
                    device_os = ANDROID
                elif IOS in lines[0]:
                    device_os = IOS
                else:
                    device_os = UNKNOWN

                # get overall result
                overall_result = CLEAN
                if any([x for x in lines if "WARNING" in x]):
                    overall_result = WARNING

                # get the date when the scan was produced
                scan_date_string = lines[0].split(" ")[0]
                scan_date = datetime.strptime(scan_date_string, "%Y-%m-%d")

                warnings = []
                for line in lines:
                    # get date of the last security update
                    if "ro.build.version.security_patch" in line:
                        patch_date_string = line.split(":")[-1].replace(" ", "").replace("\n", "")
                        patch_date = datetime.strptime(patch_date_string, "%Y-%m-%d")
                    # get all warnings
                    if "WARNING" in line:
                        warnings.append("".join([x.strip() for x in line.split("WARNING")[-1].split("-")[1:]]))
                        warnings = [x for x in warnings if x]

            # get list of apps
            applications = []
            if ANDROID in device_os:
                pass
            elif IOS in device_os:
                with open(scan_result_dir / "applications.json", "r") as f:
                    data = json.loads(f.read())

                    for item in data:
                        applications.append({
                            "app_name": item.get("itemName", "N/A"),
                            "creator": item.get("artistName", "N/A"),
                            "source": item.get("sourceApp", "N/A")
                        })

            scan_result, created = ScanResult.objects.get_or_create(
                name=scan_result_name,
                path=scan_result_dir,
                mvt_version=f"{mvt_version}",
                operating_system=device_os,
                overall_result=overall_result,
                last_security_path_date=patch_date,
                scan_date=scan_date,
                warnings="\n\n".join(set(warnings)),
                defaults={"date_added": timezone.now()}
            )

            if created and applications:
                scan_result.installed_apps = applications
                scan_result.save()

    return HttpResponseRedirect(reverse("analyzer:index"))


def delete_scan_result(request, name):
    scan_result = get_object_or_404(ScanResult, name=name)

    if request.method == "POST":
        scan_result.delete()

    return HttpResponseRedirect(reverse("analyzer:index"))


def scan_result(request, name):
    scan_result = get_object_or_404(ScanResult, name=name)

    context = {"scan_result": scan_result}

    return render(request, "analyzer/scan_result.html", context)
