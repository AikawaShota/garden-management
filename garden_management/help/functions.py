from django.conf import settings
from django.http import HttpResponse
from django.core.mail import BadHeaderError, send_mail


# 問い合わせメールの作成。
def send_inquiry_mail(
        category, subject, message, nickname, from_email, **kwargs):
    message = (
        "お問い合わせ先サイト：にわかん（https://niwakan.mesekit.com）\n"
        f"お問い合わせのカテゴリ：{category}\n"
        "お問い合わせ内容：\n"
        f"{message}\n"
        "\n"
        "にわかん 管理者"
    )
    from_email = f"{nickname} <{from_email}>"
    recipient_list = [settings.EMAIL_HOST_USER]
    try:
        send_mail(subject, message, from_email, recipient_list, **kwargs)
    except BadHeaderError:
        return HttpResponse("無効なヘッダが検出されました。")
