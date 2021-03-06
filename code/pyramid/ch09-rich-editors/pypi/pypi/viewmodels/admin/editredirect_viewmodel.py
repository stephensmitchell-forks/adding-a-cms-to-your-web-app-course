from pyramid.request import Request

from pypi.services import cms_service
from pypi.viewmodels.shared.viewmodel_base import ViewModelBase


class EditRedirectViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)

        self.short_url = None
        self.url = None
        self.name = None
        self.redirect_id = int(self.request_dict.get('redirect_id', -1))
        self.redirect = cms_service.get_redirect_by_id(self.redirect_id)
        self.error = None

        if self.redirect:
            self.short_url = self.redirect.short_url
            self.url = self.redirect.url
            self.name = self.redirect.name

    def process_form(self):
        d = self.request_dict
        self.short_url = d.get('short_url')
        self.url = d.get('url')
        self.name = d.get('name')
        self.redirect_id = d.get('redirect_id')

        if not self.short_url:
            self.error = "You must specify a short url"

        if not self.redirect and cms_service.get_redirect(self.short_url):
            self.error = f"A redirect with url {self.short_url} already exists!"
        if self.redirect and not cms_service.get_redirect_by_id(self.redirect_id):
            self.error = f"A redirect with ID {self.redirect_id} was not found!"
