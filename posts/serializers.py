

from rest_framework import serializers

from .models import Project, Comment, Order, ProjectImage, Project_Type, Tariff


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'image_url', 'description', 'url', 'start_date', 'end_date', 'created_at']


class ProjectImagesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ['id', 'image_url']


class ProjectDetailSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField('get_images')

    class Meta:
        model = Project
        fields = ['id', 'title', 'images', 'image_url', 'description', 'url', 'start_date', 'end_date', 'created_at']

    def get_images(self, obj):
        project_images = obj.images.all()
        if project_images:
            image_serializers = ProjectImagesListSerializer(project_images, many=True, context=self.context)
            return image_serializers.data
        else:
            return []


class CommentSerializer(serializers.ModelSerializer):
    project = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'user', 'date', 'project', 'comment', 'rank']

    def get_project(self, obj):
        return obj.project.title


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'fullname', 'phone', 'project_type', 'tariff', 'message']


class ProjectTariffsListSerializer(serializers.ModelSerializer):
    value = serializers.SerializerMethodField()

    class Meta:
        model = Tariff
        fields = ['id', 'title', 'description', 'start_amount', 'value']

    def get_value(self, obj):
        return obj.value.value


class ProjectTypesSerializer(serializers.ModelSerializer):
    tariffs = serializers.SerializerMethodField('get_tariffs')

    class Meta:
        model = Project_Type
        fields = ['id', 'value', 'title', 'description', 'tariffs']

    def get_tariffs(self, obj):
        project_tariffs = obj.tariffs.all()
        if project_tariffs:
            tariffs_serializers = ProjectTariffsListSerializer(project_tariffs, many=True, context=self.context)
            return tariffs_serializers.data
        else:
            return []
