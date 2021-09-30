pub trait Glimpse {
    fn glimpse1() -> {
        Transpose(MatMul(𝐗  , MatMul(y, z)) = MatMul(MatMul(𝐗   , y), z));
    }

    fn glimpse2() -> {
∀, 𝚈, 𝚉. MatMul(𝐗    , ElAdd(y, z)) = (MatMul(𝐗 , y), MatMul(  , z))
    }

    fn glimpse3() -> {
∀𝐗   . Mat(𝐗 , IMatMul) = 𝐗  
    }
    
    fn glimpse4() -> {
∀𝐗 ,x y, z, w. Mat(Concat(1, 𝐗 , z), Concat(0, y, w)) = glimpsed(MatMul(𝐗  , y), glimpsed(z, w),)
    }
}

