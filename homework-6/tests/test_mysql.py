import pytest

from mysql.builder import MySQLBuilder
from data.nginx_pars import make_data
from mysql.models import Lenght, Types, Count, Val, Error


class MySQLBase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client):
        self.mysql_client = mysql_client
        self.mysql_builder = MySQLBuilder(mysql_client)


class Test(MySQLBase):

    @pytest.mark.parametrize('key, model, num_of_strs', 
                                [
                                ('lenght', Lenght, 1),
                                ('types', Types, 5),
                                ('count', Count, 10),
                                ('val', Val, 5),
                                ('error', Error, 5)
                                ]
                            )
    def test(self, file_path, key, model, num_of_strs):
        data = make_data(key, file_path)
        for i in range(len(data)):
            print(self.mysql_builder.create_string(key=key, info=data[i]))
        self.mysql_client.session.commit()
        result = self.mysql_client.session.query(model).all()
        assert len(result) == num_of_strs
