import re
from rest_framework.serializers import ValidationError


class YoutubeOnlyValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        # Ссылка из поля, которое проверяем
        url = value.get(self.field)

        # Если ссылка есть, проверяем её через регулярное выражение
        if url:
            # Шаблон разрешает только домены youtube.com и youtu.be
            youtube_pattern = r'(https?://)?(www\.)?(youtube\.com|youtu\.be)'
            if not re.match(youtube_pattern, url):
                raise ValidationError({self.field: 'Можно добавлять ссылки только на youtube.com'})
