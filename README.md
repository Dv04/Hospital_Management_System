# Hospital Management System
Statement: A technology to improve adoption by doctors, nurses and other health/administrative workers in state healthcare facilities to use the HMIS software.

First of all please install the requirements using

```python
pip3 install requirements.txt
```

## Usage

```python3
python3 server.py
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
