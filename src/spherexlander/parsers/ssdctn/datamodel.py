from __future__ import annotations

from typing import List, Optional

from lander.ext.parser import Contributor

from ..spherexdata import SpherexMetadata

__all__ = ["SpherexSsdcTnMetadata"]


class SpherexSsdcTnMetadata(SpherexMetadata):
    """Metadata container for describing SSDC-TN documents.

    This metadata is gathered from the content of the document as well as from
    configuration files provided during the build. This metadata is used to
    populate the landing page.
    """

    @property
    def ipac_lead_v2(self) -> Optional[str]:
        """The lead IPAC author."""
        for author in self.authors:
            if author.role == "IPAC Lead":
                return author
        return None

    @property
    def other_authors(self) -> List[Contributor]:
        """Additional authors."""
        return [a for a in self.authors if a.role not in {"IPAC Lead"}]