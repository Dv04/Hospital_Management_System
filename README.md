# Hospital Management System

A technology to improve adoption by doctors, nurses and other health/administrative workers in state healthcare facilities to use the HMIS software.

## Getting Started

### Prerequisites

First of all please install the requirements using

```python
pip install requirements.txt
```

### Usage

```python
python server.py
```

Optionally, if you want to set up with a virtual environment, You can create one before installing the Requirenments:

```
virtualenv venv
source venv/bin/activate
```


To log in, please use the following configurations:

Email: test@gmail.com
Password: test
Role: Doctor

OR

Email: test1@gmail.com
Password: test
Role: Reception

OR

Email: test2@gmail.com
Password: test
Role: Patient

OR

Email: test3@gmail.com
Password: test
Role: Staff



The Backend user data is stored in Hospital_users.json

URLS:
- /
- /about
- /doctor
- /staff
- /patient
- /reception
- /pharmacy


## Built With

* [Flask](https://flask.palletsprojects.com/en/2.3.x/) - The web framework used
* [Scikit-learn](https://scikit-learn.org/stable/) - Machine Learning

## Contributing

Please read [CONTRIBUTING.md](https://github.com/Dv04/Hospital_Management_System/blob/main/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/Dv04/Hospital_Management_System/tags). 

## Authors

* **Dev Sanghvi** - *Initial work* - [DevSanghvi](https://github.com/Dv04)

See also the list of [contributors](https://github.com/Dv04/Hospital_Management_System/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
