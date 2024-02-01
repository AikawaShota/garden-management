from django.conf import settings
from django.http import HttpResponse
from django.core.mail import BadHeaderError, send_mail


# メール件名作成関数。
def get_mail_subject(subject):
    subject = f"【にわかん】問い合わせ受付完了｜{subject}"
    return subject


# メール本文作成関数。
def get_mail_message(category, nickname, message):
    message = (
        "※このメールはシステムからの自動返信です。\n"
        "\n"
        f"{nickname} 様\n"
        "\n"
        "この度は\"にわかん\"へお問い合わせいただき誠にありがとうございます。\n"
        "\n"
        "以下の内容のお問い合わせを受け付けました。\n"
        "5営業日以内に当アプリ管理者より折り返しご連絡させていただきます。\n"
        "\n"
        "尚、お問い合わせ内容によっては、ご返事までにお時間をいただく場合もございます。\n"
        "あらかじめご了承ください。\n"
        "\n"
        "=== ご入力内容 =========================================================\n"
        "\n"
        "【お問い合わせ先サイト（アプリ）】\n"
        "にわかん（https://niwakan.mesekit.com）\n"
        "【お問い合わせのカテゴリ】\n"
        f"{category}\n"
        "【お問い合わせ内容】：\n"
        f"{message}\n"
        "\n"
        "========================================================================\n"  # noqa
        "\n"
        "このメールは\"にわかん\"のアプリからお問い合わせいただいた方へ自動送信しております。\n"
        "お心当たりのない方は、恐れ入りますが下記へその旨をご連絡いただけますと幸いです。\n"
        "\n"
        "========================================================================\n"  # noqa
        "\n"
        "にわかん 管理者\n"
        "E-mail:inquiry@niwakan.mesekit.com\n"
        "URL:https://niwakan.mesekit.com\n"
        "\n"
        "========================================================================\n"  # noqa
    )
    return message


# 問い合わせメールの送信関数。
def send_inquiry_mail(
        category, subject, message, nickname, from_email, **kwargs):
    message = get_mail_message(category, nickname, message)
    subject = get_mail_subject(subject)
    from_email = f"{nickname} <{from_email}>"
    recipient_list = [settings.EMAIL_HOST_USER]
    try:
        send_mail(subject, message, from_email, recipient_list, **kwargs)
    except BadHeaderError:
        return HttpResponse("無効なヘッダが検出されました。")


# ユーザに問い合わせメールを送信する関数。
def send_inquiry_mail_to_user(
        category, subject, message, nickname, recipient_address, **kwargs):
    subject = get_mail_subject(subject)
    message = get_mail_message(category, nickname, message)
    from_email = "にわかん管理者 <inquiry@niwakan.mesekit.com>"
    recipient_list = [recipient_address]
    try:
        send_mail(subject, message, from_email, recipient_list, **kwargs)
    except BadHeaderError:
        return HttpResponse("無効なヘッダが検出されました。")
