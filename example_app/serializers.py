class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
