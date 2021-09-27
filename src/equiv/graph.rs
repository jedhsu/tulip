use spaces::Discrete;

pub trait EqGraph: ProductSpace<{
    fn populate(&self);
}


