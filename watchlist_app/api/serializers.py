from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform, Review

##ModelSerializer
class ReviewSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Review
        exclude = ['watchlist']
        # fields = "__all__"

class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = WatchList
        fields = "__all__"

class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    #Nested serializers
    watchlist = WatchListSerializer(many=True, read_only=True)
    
    class Meta:
        model = StreamPlatform
        fields = "__all__"

# class StreamPlatformSerializer(serializers.ModelSerializer):
#     #Nested serializers
#     watchlist = WatchListSerializer(many=True, read_only=True)
    
#     class Meta:
#         model = StreamPlatform
#         fields = "__all__"

    #Serializer relations
    #StringRelatedField
    # watchlist = serializers.StringRelatedField(many=True)
    
    #PrimaryKeyRelatedField
    # watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    #HyperlinkedRelatedField
    # watchlist = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='movie-detail'
    # )


    

 
    





#Validation

    # fields = ['id', 'name', 'description']
    # exclude= ['active']

    #Custom Serializer Fields
    #len_name = serializers.SerializerMethodField()

    # def get_len_name(self, object):
    #     return len(object.name)

    # #Object-level validation
    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("Title and Description should be different!")
    #     else:
    #         return data

    # #Field-level validation
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short!")
    #     else:
    #         return value

##Serializer
# #Validators
# def name_length(value):
#         if len(value) < 2:
#             raise serializers.ValidationError("Name is too short!")

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

    ##Object-level validation
    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("Title and Description should be different!")
    #     else:
    #         return data

    ##Field-level validation
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short!")
    #     else:
    #         return value