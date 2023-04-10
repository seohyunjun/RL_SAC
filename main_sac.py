import gymnasium as gym
from gymnasium.wrappers import RecordVideo
from sac_torch import Agent 
import numpy as np
from utils import plot_learning_curve


if __name__=='__main__':
    env = gym.make('Humanoid-v4',render_mode='rgb_array')
    agent = Agent(input_dims = env.observation_space.shape, env=env, n_actions=env.action_space.shape[0])
    n_games = 1000000
    file_name = 'inverted_humanoid.png'
    figure_file = 'plots/' + file_name
    
    best_score = env.reward_range[0]
    score_history = []
    load_checkpoint = False
    
    if load_checkpoint:
        agent.load_models()
        env.render(mode='human')
    
    
    for i in range(n_games):
        #env = RecordVideo(env, video_folder='')
        observation, info = env.reset()
        done = False
        score = 0
        
        while not done:
            action = agent.choose_action(observation)
            observation_, reward, done, info, _ = env.step(action)
            score += reward
            agent.remember(observation, action, reward, observation_, done)
            if not load_checkpoint:
                agent.learn()
                
            observation = observation_
        score_history.append(score)
        avg_score = np.mean(score_history[-100:]) # last 100 games reward mean
        
        if avg_score > best_score:
            best_score = avg_score
            if not load_checkpoint:
                agent.save_models()
                
        print(f'episoed {i} / score {score:.1f} / avg_score {avg_score:.1f}')
        
    if not load_checkpoint:
        x = [i+1 for i in range(n_games)]
        plot_learning_curve(x, score_history, figure_file)  