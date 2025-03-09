import numpy as np 




def set_beta_schedule(schedule_name ,beta_start , beta_end , num_timesteps):
    if schedule_name == 'linear' : 
        betas = np.linspace(beta_start , beta_end , num =num_timesteps , dtype=np.float64)
        
    else: 
        NotImplementedError("Dont support schdule way : {schedule_name}")
        
    return betas 
    