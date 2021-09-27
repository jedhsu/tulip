use crate::tensor::Tensor;

/// Configuration parameters for batch normalization.
#[derive(Debug, Clone, Copy)]
pub struct BatchNormalization {
    pub cudnn_enabled: bool,
    
    pub eps: f64,
    pub momentum: f64,

    pub ws_init: super::Init,
    pub bs_init: super::Init,
}

pub struct BatchNormalize<N, D> where N: Dimension, D: Datatype {
    config: BatchNormalization;
    
    pub fn weights(&self) -> Tensor<N, D>;
}

impl Calibrate<N, D> for BatchNormalize where N: Shape, D: Datatype {
    fn forward(&self) -> Tensor<N, D>;
}

// pub trait Batch<I, N> where I: u32, N: u32 {
//     pub type N;

//     fn iter_batches(&self) -> Iter<Batch>;
//     // fn calibrate(&self) -> 
// }
