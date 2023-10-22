def first_middleware(get_response):
    print("One time initialization")
    def first_func(request):
        print("This is before view")
        response = get_response(request)
        print("This is after view")
        return response
    return first_func