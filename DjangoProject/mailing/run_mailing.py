from django.core.management.base import BaseCommand
from mailing.models import Mailing
from mailing.services import send_mailing


class Command(BaseCommand):
    help = 'Запуск всех активных рассылок'

    def handle(self, *args, **options):
        mailings = Mailing.objects.all()
        for mailing in mailings:
            result = send_mailing(mailing)
            if "success" in result:
                self.stdout.write(self.style.SUCCESS(f'Рассылка {mailing.id} обработана'))
            else:
                self.stdout.write(self.style.WARNING(f'Рассылка {mailing.id} пропущена: {result["error"]}'))
