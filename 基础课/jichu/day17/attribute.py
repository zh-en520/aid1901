# 此示例示意实例属性的用法
class Dog:
    def eat(self,food):
        print(self.color,'的',self.kinds,'正在吃',food)
        self.last_food = food
    
    def food_info(self):
        '''此示例示意显示小狗上次吃的食物信息'''
        try:
            print(self.color,'的',self.kinds,'上次吃的是',self.last_food)
        except AttributeError:
            print('发生属性错误，获取食物信息失败')

dog1 = Dog()
dog1.kinds = '京巴'#创建实例属性
dog1.color = '白色'#创建color实例属性
dog1.color = '黄色'#修改实例属性
# print(dog1.color,'的',dog1.kinds)
dog1.eat('狗粮')
dog1.food_info()

dog2 = Dog()
dog2.color = '灰白'
dog2.kinds = '哈士奇'
dog2.eat('狗粮')
dog2.food_info()