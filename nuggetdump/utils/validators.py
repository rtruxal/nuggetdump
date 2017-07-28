class ServerValidators(object):

    @staticmethod
    def validate_server_instantiation_args(myaddr, blacklist, whitelist, redirect):
        """
        STRONG INPUT VALIDATION CUZ SERVERS B DANGEROUS.
        WILL RETURN TRUE IF CHECKS PASS, ASSERTION ERROR IF FAIL.

        :return: True or GTFO.
        """
        # addr validation
        try:
            assert isinstance(myaddr, tuple) and len(myaddr) == 2
            assert type(myaddr[0]) in (str, bytes)
            assert isinstance(myaddr[1], int) and abs(myaddr[1]) == myaddr[1]
        except AssertionError:
            raise AssertionError('there is a problem with the addr you passed into "Server"')

        # blacklist validation
        try:
            if blacklist is not None:
                assert type(blacklist) in (list, tuple, set)
                assert len(set([type(i) for i in blacklist])) in (str, bytes)
            else:
                pass
        except AssertionError:
            raise AssertionError('your blacklist is malformed. It must be an iterable strings or bytes')

        # whitelist validation
        try:
            if blacklist is not None:
                assert type(blacklist) in (list, tuple, set)
                assert len(set([type(i) for i in blacklist])) in (str, bytes)
            else:
                pass
        except AssertionError:
            raise AssertionError('your whitelist is malformed. It must be an iterable strings or bytes')

        # redirect addr validation
        try:
            if redirect is not None:
                assert isinstance(redirect, (str, bytes))
            else:
                pass
        except AssertionError:
            raise AssertionError('the redirect object passed must be an ip address within a string.')