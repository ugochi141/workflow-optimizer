import simpy
from dataclasses import dataclass
from typing import List

@dataclass
class WorkflowStep:
    name: str
    duration: float
    resources_needed: List[str]

class WorkflowOptimizer:
    def __init__(self, env):
        self.env = env
        self.workflows = {}
        self.bottlenecks = []
        
    def analyze_workflow(self, workflow_name, steps):
        """Analyze workflow for bottlenecks and optimization opportunities"""
        total_time = sum(step.duration for step in steps)
        critical_path = self.find_critical_path(steps)
        bottlenecks = self.identify_bottlenecks(steps)
        
        return {
            "workflow": workflow_name,
            "total_time": total_time,
            "critical_path": critical_path,
            "bottlenecks": bottlenecks,
            "optimization_suggestions": self.generate_suggestions(bottlenecks)
        }
    
    def find_critical_path(self, steps):
        """Identify the critical path in the workflow"""
        # Simplified - would use proper CPM algorithm
        return [step.name for step in steps if step.duration > 10]
    
    def identify_bottlenecks(self, steps):
        """Identify workflow bottlenecks"""
        bottlenecks = []
        for step in steps:
            if step.duration > 15 or len(step.resources_needed) > 2:
                bottlenecks.append({
                    "step": step.name,
                    "issue": "Long duration or resource intensive",
                    "impact": "HIGH"
                })
        return bottlenecks
    
    def generate_suggestions(self, bottlenecks):
        """Generate optimization suggestions"""
        suggestions = []
        for bottleneck in bottlenecks:
            if "resource" in bottleneck["issue"].lower():
                suggestions.append(f"Add parallel processing for {bottleneck['step']}")
            else:
                suggestions.append(f"Automate or streamline {bottleneck['step']}")
        return suggestions
    
    def simulate_optimization(self, current_workflow, proposed_changes):
        """Simulate the impact of proposed optimizations"""
        current_time = sum(step.duration for step in current_workflow)
        optimized_time = current_time * 0.7  # Assume 30% improvement
        
        return {
            "current_time": current_time,
            "optimized_time": optimized_time,
            "time_saved": current_time - optimized_time,
            "efficiency_gain": "30%"
        }
