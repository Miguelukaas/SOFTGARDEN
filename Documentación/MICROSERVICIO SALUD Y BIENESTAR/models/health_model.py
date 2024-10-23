# /app/models/health_model.py

health_records = []

def get_all_records():
    return health_records

def get_record_by_baby_id(baby_id):
    return next((record for record in health_records if record['baby_id'] == baby_id), None)

def add_health_record(baby_id, vaccines, illnesses, medication, observations):
    new_record = {
        'baby_id': baby_id,
        'vaccines': vaccines,
        'illnesses': illnesses,
        'medication': medication,
        'observations': observations
    }
    health_records.append(new_record)
    return new_record

def update_health_record(baby_id, vaccines=None, illnesses=None, medication=None, observations=None):
    record = get_record_by_baby_id(baby_id)
    if record:
        record['vaccines'] = vaccines if vaccines else record['vaccines']
        record['illnesses'] = illnesses if illnesses else record['illnesses']
        record['medication'] = medication if medication else record['medication']
        record['observations'] = observations if observations else record['observations']
    return record
