#主要实现的是用户添加、修改、删除和查询
from api.base import Base
from loguru import logger


class UserManager(Base):

    def __init__(self):
        self.add_user_url = self.get_url("/admin/admin/create")
        self.search_user_url = self.get_url("/admin/admin/list?page=1&limit=20&sort=add_time&order=desc")
        self.edit_user_url = self.get_url("/admin/admin/update")
        self.delete_user_url = self.get_url("/admin/admin/delete")

    def add_user(self,username,password,**kwargs):
        user_data={"username":username,"password":password}
        if kwargs:
            logger.info("添加管理员可选参数:{}",**kwargs)
            user_data.update(**kwargs)
        return self.post(self.add_user_url,user_data)


    def search_user(self):
        return self.get(self.search_user_url)

    def edit_user(self,id,username,password,**kwargs):
        user_data={"id":id,"username":username,"password":password}
        if kwargs:
            user_data.update(**kwargs)
        return self.post(self.edit_user_url,user_data)


    def delete_user(self,id,username,**kwargs):
        user_data={"id":id,"username":username}
        if kwargs:
            user_data.updata(**kwargs)
        return self.post(self.delete_user_url,user_data)


