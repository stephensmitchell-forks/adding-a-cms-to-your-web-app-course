from pypi_org.services import cms_service
from pypi_org.viewmodels.shared.viewmodelbase import ViewModelBase


class EditRedirectViewModel(ViewModelBase):
    def __init__(self, redirect_id: int = 0):
        super().__init__()

        # {'name': 'Talk Python',
        # 'short_url': 'talk',
        # 'url': 'https://talkpython.fm',
        # 'id': ''}

        self.redirect_id = redirect_id
        self.redirect = None
        self.name = ''
        self.url = ''
        self.short_url = ''

        if self.redirect_id:
            self.redirect = cms_service.get_redirect_by_id(self.redirect_id)

        if self.redirect:
            self.name = self.redirect.name
            self.url = self.redirect.url
            self.short_url = self.redirect.short_url

    def process_form(self):
        d = self.request_dict
        self.name = d.get('name', '').strip()
        self.url = d.get('url', '').strip()
        self.short_url = d.get('short_url', '').strip().lower()

    def validate(self) -> bool:
        if not self.name or not self.name.strip():
            self.error = 'You must specify a name.'
            return False

        if not self.url or not self.url.strip():
            self.error = 'You must specify a url.'
            return False

        if not self.short_url or not self.short_url.strip():
            self.error = 'You must specify a short url.'
            return False

        if self.redirect_id and not self.redirect:
            self.error = f"The redirect with ID {self.redirect_id} doesn't exist."
            return False

        if not self.redirect_id and cms_service.get_redirect(self.short_url):
            self.error = f"The redirect with url /{self.short_url} already exists."
            return False

        return True
