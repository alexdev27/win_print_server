from fastapi import APIRouter
from .functions import print_steakhouse_order
from .schemes import RequestStrings


datamax_router = APIRouter()


@datamax_router.post('/steakhouse/order', summary='Send list of strings to printer')
def steakhouse_order(data: RequestStrings):
    print_steakhouse_order(data.dict()['data'])
