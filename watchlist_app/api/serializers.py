from rest_framework import serializers
from ..models import Movie


class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Movie
        fields = "__all__" # Call all fields from Movie 
        # alternate fields = ['id','name','description']
        # exclude = ['active']
        
    def validate(self, data):
        if data['name'] == data['descriptio']:
            raise serializers.ValidationError('Title and Description should not be the same')

    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short!")
        else:
            return value

















# def name_length(self, value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is too short!")
#     else:
#         return value

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=50, validators=[name_length]) # Field level validation
#     description = serializers.CharField(max_length=100)
#     active = serializers.BooleanField(default=True)

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     def validate(self, data):
#         if data['title'] == data['description']:
#             raise serializers.ValidationError("Title and Description should be different.")
#         else:
#             return data
    
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short!")
    #     else:
    #         return value