from rest_framework import serializers
from .models import  student
from django.template.defaultfilters import slugify
class studentSerializer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField()
    class Meta:
        model=student
        fields=['id','name','roll','city','slug']


    def get_slug(self,obj):
         return slugify(obj.name)
import re
def validate(self, data):
        print( data )
        if data.get( 'name' ):
            name = data['name']
            special_char = re.compile('[@_!#$%^&*()<>?/\|}{~:]' )
            if len(name ) < 3:
                raise serializers.ValidationError( 'todo title must be more than 3 char' )

            if not special_char.search(name ) == None:
                raise serializers.ValidationError( 'cannot contain special characters' )

        return data