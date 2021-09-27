pub trait Rewrite {
    pub type Left;
    pub type RIght;

    fn apply(
        &self,
        expr: Expr,
    );

    fn matchleft(
        &self,
        expr: Expr,
    ) -> impl Fn<Left, SubExpr>;
}
