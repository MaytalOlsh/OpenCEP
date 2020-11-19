"""
This file contains the class responsible for parallel execution platform initialization.
"""
from parallel.ParallelExecutionParameters import ParallelExecutionParameters
from parallel.ParallelExecutionPlatforms import ParallelExecutionPlatforms
from parallel.platform.ThreadingParallelExecutionPlatform import ThreadingParallelExecutionPlatform
from parallel.manager.SequentialEvaluationManager import SequentialEvaluationManager

class PlatformFactory:
    """
    Creates a parallel execution platform given its specification.
    """
    @staticmethod
    def create_parallel_execution_platform(parallel_execution_params: ParallelExecutionParameters):
        if parallel_execution_params is None:
            parallel_execution_params = ParallelExecutionParameters()
        if parallel_execution_params.platform == ParallelExecutionPlatforms.THREADING:
            # 19.11
            threads = []
            numThread = parallel_execution_params.numThreads
            for i in range(numThread):
                t = ThreadingParallelExecutionPlatform.create_parallel_execution_unit(i, SequentialEvaluationManager, 2,   )
                t.start()
                threads.append(t)
            return threads
        raise Exception("Unknown parallel execution platform: %s" % (parallel_execution_params.platform,))
