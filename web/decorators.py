from django.utils.translation import ugettext_lazy as _


def benchmark(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end - start))
        return return_value

    return wrapper


def lastpost_widget(func):
    # Декоратор обавляющий в контекст данные для вывода виджета "последние статьи"
    def wrapper(self, request, *args, **kwargs):
        # print "user-only", request.user
        if request.META['HTTP_AUTH'] == settings.HTTP_AUTH_USER:
            return func(self, request, *args, **kwargs) or self.response
        else:
            self.response.add_error(status.ERROR_CODE_1001_WRONG_TOKEN,
                                    reason=_('User token error'),
                                    subject="X-Auth-Token")
            return self.response
    return wrapper