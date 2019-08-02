from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveUpdateAPIView, \
    RetrieveUpdateDestroyAPIView, UpdateAPIView


class BaseListCreateAPIView(ListCreateAPIView):

    def perform_create(self, serializer):
        super().perform_create(serializer)
        serializer.save(created_by=self.request.user)


class BaseCreateAPIView(CreateAPIView):

    def perform_create(self, serializer):
        super().perform_create(serializer)
        serializer.save(created_by=self.request.user)


class BaseRetrieveUpdateAPIView(RetrieveUpdateAPIView):

    def perform_update(self, serializer):
        super().perform_update(serializer)
        serializer.save(created_by=self.request.user)


class BaseRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):

    def perform_update(self, serializer):
        super().perform_update(serializer)
        serializer.save(created_by=self.request.user)


class BaseUpdateAPIView(UpdateAPIView):

    def perform_update(self, serializer):
        super().perform_update(serializer)
        serializer.save(created_by=self.request.user)
