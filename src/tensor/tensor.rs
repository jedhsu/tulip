pub trait Tensor<D, S>
where
    D: Datatype,
    S: Shape,
{
}

/// could use a dynamic scripting lang here for more "static" checks
pub trait Shape<A, B> {}

pub trait Tensor1<DT, A>
where
    DT: Datatype,
    A: Number,
{
}

pub trait Tensor2<DT, A, B>
where
    DT: Datatype,
    A: Number,
    B: Number,
{
}

pub trait Tensor3<DT, A, B, C>
where
    DT: Datatype,
    A: Number,
    B: Number,
    C: Number,
{
}

pub trait Tensor4<DT, A, B, C, D>
where
    DT: Datatype,
    A: Number,
    B: Number,
    C: Number,
    D: Number,
{
}

pub trait Tensor5<DT, A, B, C, D, E>
where
    DT: Datatype,
    A: Number,
    B: Number,
    C: Number,
    D: Number,
    E: Number,
{
}

pub trait Tensor6<DT, A, B, C, D, E, F>
where
    DT: Datatype,
    A: Number,
    B: Number,
    C: Number,
    D: Number,
    E: Number,
    F: Number,
{
}

pub trait Tensor7<DT, A, B, C, D, E, F, G>
where
    DT: Datatype,
    A: Number,
    B: Number,
    C: Number,
    D: Number,
    E: Number,
    F: Number,
    G: Number,
{
}

pub trait Tensor8<DT, A, B, C, D, E, F, G, H>
where
    DT: Datatype,
    A: Number,
    B: Number,
    C: Number,
    D: Number,
    E: Number,
    F: Number,
    G: Number,
    H: Number,
{
}
