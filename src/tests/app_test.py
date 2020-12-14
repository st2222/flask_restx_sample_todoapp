import pytest
import werkzeug


def test_create(TodoDAOMock):
    # create a table for the stub
    data = {'task': 'hello1'}
    res = TodoDAOMock.create(data)
    assert res['task'] == 'hello1'


def test_get(TodoDAOMock):
    # create a table for the stub
    data = {'task': 'hello1'}
    TodoDAOMock.create(data)
    assert TodoDAOMock.get(1)['task'] == 'hello1'


def test_get_list(TodoDAOMock):
    # create a table for the stub
    assert TodoDAOMock.get_list() == []
    data = {'task': 'hello1'}
    TodoDAOMock.create(data)
    assert len(TodoDAOMock.get_list()) == 1


def test_update(TodoDAOMock):
    # create a table for the stub
    data1 = {'task': 'hello1'}
    TodoDAOMock.create(data1)
    assert TodoDAOMock.get(1)['task'] == 'hello1'
    data2 = {'task': 'hello2'}
    TodoDAOMock.update(1, data2)
    assert TodoDAOMock.get(1)['task'] == 'hello2'


def test_delete(TodoDAOMock):
    data1 = {'task': 'hello1'}
    TodoDAOMock.create(data1)
    assert TodoDAOMock.get(1)['task'] == 'hello1'
    TodoDAOMock.delete(1)
    with pytest.raises(Exception):
        assert TodoDAOMock.get(1)
