import unittest
from api.user_manager import UserManager
from data.user_manager_data import UserManagerData

from loguru import logger
class TestUserManager(unittest.TestCase):
    user_Id=0

    @classmethod
    def setUpClass(cls) -> None:
        cls.user=UserManager()
        cls.user.login()
        cls.username=UserManagerData.add_user_data.get("username")
        cls.new_username = UserManagerData.add_user_data.get("new_user_name")
        cls.password=UserManagerData.add_user_data.get("password")


    def test01_add_user(self):
        #初始化添加管理员的测试数据
        #self.password="123456"
        #self.user_id=None
        #self.user_name="testa1"
        #调用添加管理员接口
        actual_result=self.user.add_user(self.username,self.password)
        data=actual_result.get('data')
        if data:
            self.user_id=data.get('id')
            TestUserManager.user_id=self.user_id
        # 进行断言
        self.assertEqual(0,actual_result['errno'])
        self.assertEqual(self.username,actual_result.get('data').get('username'))




    def test02_edit_user(self):

        actual_result=self.user.edit_user(TestUserManager.user_id,self.new_username,password=123456)
        #断言
        self.assertEqual(0, actual_result['errno'])
        self.assertEqual(self.new_username,actual_result.get('data').get('username'))


    def test03_search_user(self):
        actual_result=self.user.search_user()
        self.assertEqual(0, actual_result['errno'])
        self.assertEqual(self.new_username,actual_result.get('data').get('list')[0].get('username'))


    def test04_delete_user(self):
        actual_result=self.user.delete_user(TestUserManager.user_id,self.new_username)
        self.assertEqual(0, actual_result['errno'])



if __name__ == '__main__':
    unittest.main()

