impl Extractor for LpExtractor {
    fn extract(&self) -> {
        let enodes = &self.nodes().iter();
        let eclasses = &self.classes().iter();

        let enodes_inside = |ecls| enodes.inside(ecls);

        let children = |enode| enode.children();


    }

}
