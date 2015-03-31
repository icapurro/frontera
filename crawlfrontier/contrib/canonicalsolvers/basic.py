# -*- coding: utf-8 -*-
from crawlfrontier.core.components import CanonicalSolver
from pdb import set_trace

class BasicCanonicalSolver(CanonicalSolver):
    """
    Implements a simple CanonicalSolver taking always first URL from redirect chain, if there were redirects.
    It allows easily to avoid leaking of requests in CF (e.g. when request issued by
    :attr:`get_next_requests() <crawlfrontier.core.manager.FrontierManager.get_next_requests>` never matched in
    :attr:`page_crawled() <crawlfrontier.core.manager.FrontierManager.page_crawled>`) at the price of duplicating
    records in CF for pages having more than one URL or complex redirects chains.
    """
    def frontier_start(self):
        pass

    def frontier_stop(self):
        pass

    def add_seeds(self, seeds):
        pass

    def page_crawled(self, response, links):
        pass

    def request_error(self, page, error):
        pass

    def get_canonical_url(self, obj):
        canonical_url = obj.url
        canonical_fingerprint = obj.meta['fingerprint']
        if 'redirect_urls' in obj.meta:
            redirect_urls = obj.meta['redirect_urls']
            redirect_fingerprints = obj.meta['redirect_fingerprints']
            redirect_urls.append(obj.url)
            redirect_fingerprints.append(obj.meta['fingerprint'])

            canonical_url = redirect_urls[0]
            canonical_fingerprint = redirect_fingerprints[0]
        return (canonical_url, canonical_fingerprint)