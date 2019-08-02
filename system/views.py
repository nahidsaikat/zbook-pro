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


class BaseRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):

    def get_serializer_context(self):
        contest = super().get_serializer_context()
        contest['request'] = self.request
        return contest


class BaseUpdateAPIView(UpdateAPIView):

    def get_serializer_context(self):
        contest = super().get_serializer_context()
        contest['request'] = self.request
        return contest
