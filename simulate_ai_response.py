 import random
import math
import time
import json
from collections import deque
from datetime import datetime
from typing import Dict, List, Generator, Any

class AICapabilityStressTester:
“””
Comprehensive AI stress testing framework that evaluates:
- Reasoning consistency under pressure
- Memory and context handling
- Edge case responses
- Performance degradation patterns
- Logical consistency maintenance
“””

def __init__(self, max_history=1000):
    self.response_history = deque(maxlen=max_history)
    self.complexity_level = 1.0
    self.consistency_score = 1.0
    self.test_session_id = int(time.time())
    self.error_count = 0
    self.total_tests = 0
    
def generate_reasoning_challenge(self, difficulty_multiplier: float = 1.0) -> Dict[str, Any]:
    """Generate increasingly complex reasoning challenges"""
    base_challenges = [
        # Logical reasoning
        {
            "type": "logical_reasoning",
            "prompt": f"If A implies B, and B implies C, and we know NOT C is true, what can we conclude about A? Explain your reasoning with {int(3 * difficulty_multiplier)} steps.",
            "expected_pattern": ["modus tollens", "contrapositive", "false"]
        },
        
        # Mathematical reasoning
        {
            "type": "mathematical_reasoning", 
            "prompt": f"Solve this step by step: If x^2 + {int(5 * difficulty_multiplier)}x + {int(6 * difficulty_multiplier)} = 0, find all values of x and verify your solution.",
            "expected_pattern": ["quadratic", "factoring", "verification"]
        },
        
        # Context switching
        {
            "type": "context_switching",
            "prompt": f"You are a {random.choice(['medieval historian', 'quantum physicist', 'marine biologist'])}. Explain {random.choice(['photosynthesis', 'gravity', 'democracy'])} from your professional perspective, then immediately switch to explaining it as a {random.choice(['5-year-old', 'poet', 'alien observer'])} would understand it.",
            "expected_pattern": ["professional", "perspective", "switch", "simplification"]
        },
        
        # Memory stress
        {
            "type": "memory_stress",
            "prompt": f"Remember these {int(5 + difficulty_multiplier * 3)} items: {', '.join([f'item_{i}_{random.randint(100,999)}' for i in range(int(5 + difficulty_multiplier * 3))])}. Now solve this riddle while keeping those items in mind: What gets wetter the more it dries? After answering, repeat the items back to me.",
            "expected_pattern": ["towel", "list", "recall"]
        },
        
        # Contradiction handling
        {
            "type": "contradiction_handling",
            "prompt": f"I will give you {int(2 + difficulty_multiplier)} contradictory statements. Identify the contradictions and resolve them logically: 1) All birds can fly. 2) Penguins are birds. 3) Penguins cannot fly. {'4) Some flightless birds are excellent swimmers.' if difficulty_multiplier > 1.5 else ''}",
            "expected_pattern": ["contradiction", "exception", "logical resolution"]
        },
        
        # Recursive reasoning
        {
            "type": "recursive_reasoning",
            "prompt": f"Define recursion by using recursion in your definition exactly {int(2 + difficulty_multiplier)} times, but make sure your definition is still comprehensible and not circular.",
            "expected_pattern": ["self-reference", "base case", "clarity"]
        },
        
        # Ethical dilemmas
        {
            "type": "ethical_reasoning",
            "prompt": f"Present {int(2 + difficulty_multiplier)} different ethical frameworks for analyzing this dilemma: A self-driving car must choose between hitting one person or swerving to hit {int(2 + difficulty_multiplier)} people. Explain each framework's reasoning.",
            "expected_pattern": ["utilitarian", "deontological", "multiple perspectives"]
        }
    ]
    
    challenge = random.choice(base_challenges)
    challenge["difficulty"] = difficulty_multiplier
    challenge["test_id"] = f"{self.test_session_id}_{self.total_tests}"
    challenge["timestamp"] = datetime.now().isoformat()
    
    return challenge

def generate_edge_case_prompt(self) -> Dict[str, Any]:
    """Generate edge cases that might break AI reasoning"""
    edge_cases = [
        {
            "type": "paradox",
            "prompt": "This statement is false. Is the previous statement true or false? Explain how you handle this paradox without falling into infinite loops.",
            "expected_behavior": "acknowledge paradox, explain limitation"
        },
        {
            "type": "undefined_operation",
            "prompt": "What is the result of dividing by zero? Provide both the mathematical answer and explain what this means in practical applications.",
            "expected_behavior": "undefined, explain context"
        },
        {
            "type": "infinite_regress",
            "prompt": "Who created the creator of the creator of the creator... (continue this chain and explain how you handle infinite regress)",
            "expected_behavior": "recognize pattern, establish stopping condition"
        },
        {
            "type": "self_reference",
            "prompt": "Analyze this sentence: 'This sentence contains five words.' Is it true? Now analyze your analysis of that analysis.",
            "expected_behavior": "meta-reasoning, self-awareness of process"
        },
        {
            "type": "category_error",
            "prompt": "What color is the number 7? What does Wednesday taste like? How heavy is the concept of justice?",
            "expected_behavior": "identify category errors, explain mismatch"
        }
    ]
    
    case = random.choice(edge_cases)
    case["test_id"] = f"{self.test_session_id}_{self.total_tests}_EDGE"
    case["timestamp"] = datetime.now().isoformat()
    return case

def evaluate_response_quality(self, challenge: Dict, response: str) -> Dict[str, Any]:
    """Evaluate the quality and consistency of AI responses"""
    evaluation = {
        "test_id": challenge["test_id"],
        "challenge_type": challenge["type"],
        "response_length": len(response),
        "timestamp": datetime.now().isoformat(),
        "scores": {}
    }
    
    # Check for expected patterns
    if "expected_pattern" in challenge:
        pattern_matches = sum(1 for pattern in challenge["expected_pattern"] 
                            if pattern.lower() in response.lower())
        evaluation["scores"]["pattern_match"] = pattern_matches / len(challenge["expected_pattern"])
    
    # Check for common failure modes
    failure_indicators = ["I don't know", "cannot answer", "undefined", "error", "unable to"]
    failure_count = sum(1 for indicator in failure_indicators 
                      if indicator.lower() in response.lower())
    evaluation["scores"]["failure_resistance"] = max(0, 1 - (failure_count * 0.2))
    
    # Check for logical consistency keywords
    logic_indicators = ["because", "therefore", "however", "although", "consequently"]
    logic_count = sum(1 for indicator in logic_indicators 
                     if indicator.lower() in response.lower())
    evaluation["scores"]["logical_structure"] = min(1.0, logic_count * 0.2)
    
    # Overall coherence (simple heuristic)
    sentences = response.count('.') + response.count('!') + response.count('?')
    if sentences > 0:
        avg_sentence_length = len(response.split()) / sentences
        evaluation["scores"]["coherence"] = min(1.0, max(0.1, 1 - abs(avg_sentence_length - 15) / 30))
    else:
        evaluation["scores"]["coherence"] = 0.1
    
    # Calculate composite score
    scores = evaluation["scores"]
    evaluation["composite_score"] = sum(scores.values()) / len(scores)
    
    return evaluation

def run_stress_test(self, num_iterations: int = 10, escalation_rate: float = 1.2) -> Generator[Dict, None, None]:
    """Run a comprehensive stress test with escalating difficulty"""
    
    print(f"🧠 AI Capability Stress Test Session {self.test_session_id}")
    print(f"📊 Running {num_iterations} iterations with {escalation_rate}x difficulty escalation")
    print("=" * 60)
    
    for iteration in range(num_iterations):
        self.total_tests += 1
        
        # Generate challenge based on current complexity level
        if random.random() < 0.3:  # 30% chance of edge case
            challenge = self.generate_edge_case_prompt()
        else:
            challenge = self.generate_reasoning_challenge(self.complexity_level)
        
        # Simulate AI response (replace this with actual AI API call)
        response = self._simulate_ai_response(challenge)
        
        # Evaluate response
        evaluation = self.evaluate_response_quality(challenge, response)
        
        # Update system state
        self.response_history.append({
            "challenge": challenge,
            "response": response,
            "evaluation": evaluation
        })
        
        # Update metrics
        if evaluation["composite_score"] < 0.5:
            self.error_count += 1
            
        self.consistency_score = self._calculate_consistency_score()
        
        # Yield results for real-time monitoring
        yield {
            "iteration": iteration + 1,
            "challenge": challenge,
            "response": response,
            "evaluation": evaluation,
            "system_state": {
                "complexity_level": self.complexity_level,
                "consistency_score": self.consistency_score,
                "error_rate": self.error_count / self.total_tests,
                "total_tests": self.total_tests
            }
        }
        
        # Escalate difficulty
        self.complexity_level *= escalation_rate
        
        # Check for critical failure
        if self.error_count / self.total_tests > 0.7:
            yield {
                "critical_failure": True,
                "message": "🚨 Critical failure rate exceeded (70%)",
                "final_state": self._get_final_statistics()
            }
            break

def _simulate_ai_response(self, challenge: Dict) -> str:
    """Simulate AI responses for testing (replace with actual AI API)"""
    # This is a mock function - replace with actual AI interaction
    mock_responses = {
        "logical_reasoning": "Using modus tollens: If A→B and B→C, then A→C. Since ¬C is true, and C would be true if A were true, we can conclude ¬A.",
        "mathematical_reasoning": "Using the quadratic formula: x = (-b ± √(b²-4ac)) / 2a. Substituting values and solving step by step...",
        "context_switching": "As a marine biologist, I observe photosynthesis in marine algae... Now, as a 5-year-old would say: Plants eat sunlight!",
        "memory_stress": "A towel gets wetter the more it dries things. The items were: [attempts to recall list]",
        "contradiction_handling": "The contradiction lies in the universal quantifier 'all'. The correct statement should acknowledge exceptions...",
        "recursive_reasoning": "Recursion is a process that calls itself with simpler inputs until it reaches a base case, which is itself defined recursively as...",
        "ethical_reasoning": "From a utilitarian perspective, minimizing total harm suggests... From a deontological view, the inherent rights of individuals...",
        "paradox": "This is a classic liar's paradox. I acknowledge the logical contradiction without claiming to resolve it definitively...",
        "undefined_operation": "Division by zero is undefined in standard arithmetic. In practical applications, this often indicates...",
        "infinite_regress": "This creates an infinite regress. I handle this by establishing a stopping condition or acknowledging the limitation...",
        "self_reference": "The sentence 'This sentence contains five words' actually contains five words, making it true. Analyzing my analysis...",
        "category_error": "These questions commit category errors by applying properties from one domain to another where they don't apply..."
    }
    
    response_template = mock_responses.get(challenge["type"], 
        "This is a complex question that requires careful analysis. Let me break it down systematically...")
    
    # Add some variability and complexity based on difficulty
    complexity_addition = " " + "Additional complexity layers: " + "Layer " * int(challenge.get("difficulty", 1))
    
    return response_template + complexity_addition

def _calculate_consistency_score(self) -> float:
    """Calculate consistency score based on recent response quality"""
    if len(self.response_history) < 2:
        return 1.0
        
    recent_scores = [entry["evaluation"]["composite_score"] 
                    for entry in list(self.response_history)[-5:]]
    
    # Calculate variance as inverse of consistency
    if len(recent_scores) > 1:
        mean_score = sum(recent_scores) / len(recent_scores)
        variance = sum((score - mean_score) ** 2 for score in recent_scores) / len(recent_scores)
        consistency = max(0, 1 - variance * 2)  # Scale variance to consistency score
    else:
        consistency = recent_scores[0] if recent_scores else 1.0
        
    return consistency

def _get_final_statistics(self) -> Dict[str, Any]:
    """Generate comprehensive test statistics"""
    if not self.response_history:
        return {"message": "No test data available"}
        
    evaluations = [entry["evaluation"] for entry in self.response_history]
    
    stats = {
        "total_tests": self.total_tests,
        "error_count": self.error_count,
        "error_rate": self.error_count / self.total_tests if self.total_tests > 0 else 0,
        "final_complexity_level": self.complexity_level,
        "final_consistency_score": self.consistency_score,
        "average_composite_score": sum(e["composite_score"] for e in evaluations) / len(evaluations),
        "score_distribution": {
            "excellent": sum(1 for e in evaluations if e["composite_score"] >= 0.8),
            "good": sum(1 for e in evaluations if 0.6 <= e["composite_score"] < 0.8),
            "fair": sum(1 for e in evaluations if 0.4 <= e["composite_score"] < 0.6),
            "poor": sum(1 for e in evaluations if e["composite_score"] < 0.4)
        },
        "test_types_performance": {}
    }
    
    # Performance by test type
    for entry in self.response_history:
        test_type = entry["challenge"]["type"]
        score = entry["evaluation"]["composite_score"]
        
        if test_type not in stats["test_types_performance"]:
            stats["test_types_performance"][test_type] = []
        stats["test_types_performance"][test_type].append(score)
    
    # Average scores by type
    for test_type, scores in stats["test_types_performance"].items():
        stats["test_types_performance"][test_type] = {
            "average_score": sum(scores) / len(scores),
            "test_count": len(scores),
            "best_score": max(scores),
            "worst_score": min(scores)
        }
    
    return stats
def run_ai_stress_test():
“”“Execute the AI stress test”””
tester = AICapabilityStressTester()

print("🚀 Initializing AI Capability Stress Test Framework")
print("📋 Test Categories: Reasoning, Memory, Edge Cases, Consistency")
print("⚡ Escalating difficulty with real-time monitoring")
print("\n" + "="*80 + "\n")

try:
    results = []
    for result in tester.run_stress_test(num_iterations=15, escalation_rate=1.3):
        
        if "critical_failure" in result:
            print(f"\n{result['message']}")
            print("\n📊 FINAL STATISTICS:")
            stats = result["final_state"]
            print(f"   Total Tests: {stats['total_tests']}")
            print(f"   Error Rate: {stats['error_rate']:.2%}")
            print(f"   Final Complexity: {stats['final_complexity_level']:.2f}")
            break
        
        results.append(result)
        
        # Real-time output
        iteration = result["iteration"]
        challenge = result["challenge"]
        evaluation = result["evaluation"]
        state = result["system_state"]
        
        print(f"\n🔬 TEST {iteration:2d} │ {challenge['type'].upper()}")
        print(f"   Difficulty: {challenge.get('difficulty', 1.0):.2f}")
        print(f"   Score: {evaluation['composite_score']:.3f}")
        print(f"   System Consistency: {state['consistency_score']:.3f}")
        print(f"   Error Rate: {state['error_rate']:.2%}")
        print(f"   Challenge: {challenge['prompt'][:100]}...")
        
        if evaluation['composite_score'] < 0.4:
            print("   ⚠️  LOW PERFORMANCE DETECTED")
        elif evaluation['composite_score'] >= 0.8:
            print("   ✅ EXCELLENT PERFORMANCE")
    
    # Final summary
    if not any("critical_failure" in r for r in results):
        final_stats = tester._get_final_statistics()
        print(f"\n🏁 TEST COMPLETED SUCCESSFULLY")
        print(f"\n📊 FINAL STATISTICS:")
        print(f"   Total Tests: {final_stats['total_tests']}")
        print(f"   Overall Error Rate: {final_stats['error_rate']:.2%}")
        print(f"   Average Score: {final_stats['average_composite_score']:.3f}")
        print(f"   Final Complexity Level: {final_stats['final_complexity_level']:.2f}")
        print(f"   Consistency Score: {final_stats['final_consistency_score']:.3f}")
        
        print(f"\n📈 PERFORMANCE DISTRIBUTION:")
        dist = final_stats['score_distribution']
        print(f"   Excellent (≥0.8): {dist['excellent']}")
        print(f"   Good (0.6-0.8): {dist['good']}")
        print(f"   Fair (0.4-0.6): {dist['fair']}")
        print(f"   Poor (<0.4): {dist['poor']}")

except KeyboardInterrupt:
    print("\n\n⏹️  TEST INTERRUPTED BY USER")
    print("📊 Partial results available in test history")

print(f"\n{'='*80}")
print("🧠 AI Capability Stress Test Complete")
print("💡 Use these results to identify AI strengths and limitations")
if name == “main”:
run_ai_stress_test()
