__author__ = 'ikalinka'
import requests
import pytest
import json

qa_url='http://qainterview.cogniance.com/'
data = {"name": "Igor", "position": "QA"}
header = {'content-type': 'application/json'}

def test_get_candidate():
    r = requests.get(qa_url+'candidates')
    assert r.status_code == 200, 'Status is not 200'

def test_post_candidate(): # comment
    r = requests.post(qa_url+'candidates', data=json.dumps(data), headers = header)
    assert r.status_code == 201, 'Status is not 201'

def test_get_candidateID():
    r = requests.get(qa_url+'candidates/40')
    assert r.status_code == 200, 'Status is not 200'

def test_delete_candidate():
    r = requests.delete(qa_url+'candidates/50')
    assert r.status_code == 200, 'Status is not 200'

if __name__ == '__main__':
    pytest.main([__file__, '-v'])