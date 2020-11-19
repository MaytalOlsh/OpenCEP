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
    def create_parallel_execution_platform(patterns: Pattern or List[Pattern], eval_mechanism_params: EvaluationMechanismParameters, parallel_execution_params: ParallelExecutionParameters):
        if parallel_execution_params is None:
            parallel_execution_params = ParallelExecutionParameters()
        if parallel_execution_params.platform == ParallelExecutionPlatforms.THREADING:
            # 19.11
            threads = []
            numThread = parallel_execution_params.numThreads
            k_dict = {
                "patterns": patterns,
                "eval_mechanism_params": eval_mechanism_params
            }
            for i in range(numThread):
                t = ThreadingParallelExecutionPlatform.create_parallel_execution_unit(unit_id=i,callback_function= SequentialEvaluationManager,kwargs= *k_dict  )
                t.start()
                threads.append(t)
            return threads
        raise Exception("Unknown parallel execution platform: %s" % (parallel_execution_params.platform,))
