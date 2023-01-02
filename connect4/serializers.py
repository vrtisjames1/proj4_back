from rest_framework import serializers 
from .models import Connect4

class Connect4Serializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Connect4 # tell django which model to use
        fields = ('id','game_name','winner', 'username1', 'user1_turn', 'username2', 'user2_turn','a1','a2','a3','a4','a5','a6','a7','b1','b2','b3','b4','b5','b6','b7','c1','c2','c3','c4','c5','c6','c7','c1','c2','c3','c4','c5','c6','c7','d1','d2','d3','d4','d5','d6','d7','e1','e2','e3','e4','e5','e6','e7','f1','f2','f3','f4','f5','f6','f7',) 