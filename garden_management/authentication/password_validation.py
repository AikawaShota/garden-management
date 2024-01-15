from django.core.exceptions import ValidationError
import re


class CustomValidator:
    message = "パスワードは（英大文字・英小文字・数字・記号）のいずれか2つ以上を組み合わせて設定してください。"

    def validate(self, password, user=None):
        type_count = sum([
            True if re.search('[0-9]', password) is not None else False,
            True if re.search('[a-z]', password) is not None else False,
            True if re.search('[A-Z]', password) is not None else False,
            True if re.search('[^0-9a-zA-Z]', password) is not None else False
        ])
        if type_count < 2:
            raise ValidationError(self.message)

    def get_help_text(self):
        return self.message
