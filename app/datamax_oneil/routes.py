from fastapi import APIRouter
from .functions import print_steakhouse_order
from typing import List

datamax_router = APIRouter()


@datamax_router.post('/steakhouse/order', summary='Send list of strings to printer')
def steakhouse_order(data: List[str]):
    print_steakhouse_order(data)
