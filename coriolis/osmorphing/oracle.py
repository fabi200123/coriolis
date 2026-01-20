# Copyright 2016 Cloudbase Solutions Srl
# All Rights Reserved.

from coriolis.osmorphing.osdetect import oracle as oracle_detect
from coriolis.osmorphing import redhat


ORACLE_DISTRO_IDENTIFIER = oracle_detect.ORACLE_DISTRO_IDENTIFIER


class BaseOracleMorphingTools(redhat.BaseRedHatMorphingTools):

    @classmethod
    def check_os_supported(cls, detected_os_info):
        if detected_os_info['distribution_name'] != (
                ORACLE_DISTRO_IDENTIFIER):
            return False
        return cls._version_supported_util(
            detected_os_info['release_version'], minimum=6)
