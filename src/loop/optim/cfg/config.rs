pub trait Configuration {
    pub type Cfg;

    fn config() -> Self::Cfg;
}
