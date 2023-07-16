# MVT-companion

This is a Proof of Concept web app meant to serve as a companion to the [Mobile Verification Toolkit](https://github.com/mvt-project/mvt). 

The **Mobile Verification Toolkit** has been developed and released by the [Amnesty International Security Lab](https://www.amnesty.org/en/tech/) in July 2021 in the context of the [Pegasus Project](https://forbiddenstories.org/about-the-pegasus-project/) along with [a technical forensic methodology](https://www.amnesty.org/en/latest/research/2021/07/forensic-methodology-report-how-to-catch-nso-groups-pegasus/). 

**MVT-companion** was developed by [catileptic](https://github.com/catileptic) during her Fellowship with the Amnesty International Security Lab. It is meant to be used to visualize the results of MVT scans. 

## Components

**MVT-companion** is a **Django** application that uses **PostgreSQL** for storage.

## Usage

MVT-companion is meant to run as a local web app using Docker.

Build the Docker image
```
make build
```

Run the app 
```
make up
```

**To import scan results**, add a `mvt_output` dir to the root and add a dir containing all the results directly inside it.
**Make sure to do this before running `make up`**.
```
    mvt_companion
        mvt_output
            scan_person1_android
                command.log
                dumpsys_accesibility.json
                ...
            scan_person2_ios
                command.log
                accounts.json
                ...
```

Get a shell inside the MVT-companion app
```
make shell
```

Get a shell inside the Django app
```
make shell
python manage.py shell
```

If you make any modifications to `models.py` make sure to
```
make shell
python manage.py makemigrations
python manage.py migrate
```
