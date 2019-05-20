FROM jupyter/r-notebook:abdb27a6dfbb 

USER $NB_UID

RUN  conda install --quiet --yes -c conda-forge r-rpostgresql \
    conda clean -tipsy && \
    fix-permissions $CONDA_DIR

ENV CPATH=$CONDA_DIR/include

# Add conda env hook
COPY ./conda-activate.sh /usr/local/bin/before-notebook.d/
