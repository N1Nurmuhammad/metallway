from .about import AboutUsGetSerializer
from .banners import BannersGetSerializer
from .product_category import ProductsCategoryGetSerializer
from .products import ProductsGetSerializer
from .lead import LeadGetSerializer, LeadCreateSerializer
from .statistics import StatisticsGetSerializer
from .our_clients import OurClientsGetSerializer

__all__ = [
    "AboutUsGetSerializer",
    "BannersGetSerializer",
    "ProductsCategoryGetSerializer",
    "ProductsGetSerializer",
    "LeadGetSerializer",
    "LeadCreateSerializer",
    "StatisticsGetSerializer",
    "OurClientsGetSerializer",
]
