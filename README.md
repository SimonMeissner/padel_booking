Web automation script written in python using the selenium browser library.

## Getting started
- Python min. version 3.10 installed
- Create .env file with structure from .env.example and fill out credentials
- Edit the dayTimes variable inside padel_booking.py to include the hours you want to book. The array takes multiple starting hours. Example:
```python
dayTimes = [15,16,17]
```
This would try to book the slots 15:00-16:00, 16:00-17:00 and 17:00-18:00
- Finally run the script:
```bash
python3.10 padel_booking.py
```
