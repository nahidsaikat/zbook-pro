from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveUpdateAPIView, \
    RetrieveUpdateDestroyAPIView, UpdateAPIView


class BaseListCreateAPIView(ListCreateAPIView):

    def get_serializer_context(self):
        contest = super().get_serializer_context()
        contest['request'] = self.request
        return contest


class BaseCreateAPIView(CreateAPIView):

    def get_serializer_context(self):
        contest = super().get_serializer_context()
        contest['request'] = self.request
        return contest


class BaseRetrieveUpdateAPIView(RetrieveUpdateAPIView):

    def get_serializer_context(self):
        contest = super().get_serializer_context()
        contest['request'] = self.request
        return contest

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)


class BaseRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):

    def get_serializer_context(self):
        contest = super().get_serializer_context()
        contest['request'] = self.request
        return contest

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)


class BaseUpdateAPIView(UpdateAPIView):

    def get_serializer_context(self):
        contest = super().get_serializer_context()
        contest['request'] = self.request
        return contest

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)
