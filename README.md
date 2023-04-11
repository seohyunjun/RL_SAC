# RL_SAC
Soft Actor-Critic 

[SAC Code origin git](https://github.com/philtabor/Youtube-Code-Repository/tree/master/ReinforcementLearning/PolicyGradient/SAC/tf2)


## paper
----
SAC - [Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor(2018.8.8)](https://arxiv.org/abs/1801.01290)

<br>

## Code Environment
----
[OpenAI-gym](https://www.gymlibrary.dev/)
[Mujoco in M1](https://bnmy6581.tistory.com/146)
<br>
<br>

## Mac setting 
```shell
brew install cmake zlib
pip install 'gymnasium[all]'
pip install autorom # 0.42 버전 설치 (0.55 버전 mac m1 subprocess error)
AutoROM --accept-license (rom license Y 후 ale_py rom으로 파일 이동)
# mv /Users/[user_id]/[anaconda/conda/miniforge]/envs/[env_name]/lib/python3.8/site-pakage/AutoRom/rom /Users/[user_id]/[anaconda/conda/miniforge]/envs/[env_name]/lib/python3.8/site-pakage/ale_py/rom/

# require
brew install mpi4py # 
pip install tensorflow-macos # tensorflow-macos (v2 -> compat.v1 )
pip install torch
pip install gymnasium

# fix code 
# gymnasium return 2 parameter
# state, info = env.reset()
# env.step()
```

## Train
----
```bash
## SAC train
```

 
<br>

## Install Reference 

---- 

<br>

[pip install gym error](https://www.pygame.org/wiki/MacCompile)
<br>

[나만의 GYM 환경 만들기](https://www.youtube.com/watch?v=chVLag1NIAQ)
<br>

[Can a Random Reinforcement Learning Agent Maximize its Score? Soft Actor Critic (SAC) in Tensorflow2](https://www.youtube.com/watch?v=YKhkTOU0l20)
<br>


## SAC Test(Humanoid)
- tianshou benchmark (buffersize 915000, return 5341)
- [tianshou benchmark](https://tianshou.readthedocs.io/en/master/tutorials/benchmark.html#mujoco-benchmark)

<img src="https://github.com/seohyunjun/RL_TD3/blob/main/video/final7.gif" width="75%" height="75%" >

<img src="https://github.com/seohyunjun/RL_SAC/blob/main/ppt/slide1.jpeg" height=80% width=80% >
<img src="https://github.com/seohyunjun/RL_SAC/blob/main/ppt/slide2.jpeg" height=80% width=80% >
<img src="https://github.com/seohyunjun/RL_SAC/blob/main/ppt/slide3.jpeg" height=80% width=80% >
<img src="https://github.com/seohyunjun/RL_SAC/blob/main/ppt/slide4.jpeg" height=80% width=80% >
<img src="https://github.com/seohyunjun/RL_SAC/blob/main/ppt/slide5.jpeg" height=80% width=80% >
<img src="https://github.com/seohyunjun/RL_SAC/blob/main/ppt/slide6.jpeg" height=80% width=80% >
<img src="https://github.com/seohyunjun/RL_SAC/blob/main/ppt/slide7.jpeg" height=80% width=80% >
