import torch as th 














class  GaussianDiffusion :
    def __init__(self , betas ,num_timesteps , dt , betas_schedule = None):
        self.betas = betas 
        self.alpha = 1.0  - self.betas

        
        
    def q_sample(self ,  timestep , noise , x0_gt ):
        if noise == None:
            noise = th.randlike(x0_gt)
            
            